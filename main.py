import pandas as pd
import jinja2
from json import loads, dumps
import requests
from more_itertools import chunked
from xml.sax.saxutils import escape, unescape
from config import *
from secrets import cc_token


def split_formatted_filename(filename, delim='||', prefix=None):
    filenames = filename.split(delim)
    if not prefix:
        subdir = filenames[0].split(".")[0]
        prefix = "private/shareok/proquest_2008_2013_pdfs/data/{0}".format(subdir)
    return ["{0}/{1}".format(prefix, item) if prefix else item for item in filename.split(delim)]


def get_subdir(filename, delim='||'):
    """ This gets the filename without the extension of the first file.
        This is used to group related files into a single subdir
    """
    filenames = filename.split(delim)
    return filenames[0].split(".")[0]


if __name__ == '__main__':
    # TODO: update path to proquest csv file
    csv_path = "/home/tdpearson/Desktop/proquest_load.csv"

    df = pd.read_csv(csv_path, engine="python", encoding='utf-8', keep_default_na=False)
    df.columns = [col.replace(".", "_") for col in df.columns]  # replace . with _ for easier use with jinja2

    ## get specific row as df
    #df = df.loc[52:52]

    # escape xml and split multiple items out
    for element in ['dc_contributor_committee', 'dc_subject', 'dc_description_abstract', 'dc_type']:
        df[element] = df.apply(lambda x: escape(x[element]), axis=1)
        df[element] = df.apply(lambda x: x[element].split("||"), axis=1)

    # escape xml on these columns
    df['ou_group'] = df.apply(lambda x: escape(x['ou_group']), axis=1)

    env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True)
    dc_template = env.from_string(dc_xml)
    ou_template = env.from_string(ou_xml)

    chunked_records = chunked(df.to_dict(orient="record"), 10)
    for records in list(chunked_records):
        data = []
        for attributes in records:
            dc_xml = dc_template.render(**attributes)
            ou_xml = ou_template.render(**attributes)
            data.append(
                {get_subdir(attributes['filename']):
                     {"files": split_formatted_filename(attributes['filename']),
                      "metadata": dc_xml,
                      "metadata_ou": ou_xml
                      }
                 }
            )

        # TODO: Change queue to push to production
        ingest_args = {
            "function": "dspaceq.tasks.tasks.dspace_ingest",
            "queue": "shareok-dspace6x-test-workerq",
            "args": [data, "11244/62727"],
            "kwargs": {},
            "tags": []
        }


        from pprint import pprint
        pprint(ingest_args)

        # TODO: Uncomment the following to run ingest
        #headers = {'Content-Type': 'application/json', "Authorization": "Token {0}".format(cc_token)}
        #req = requests.post("https://cc.lib.ou.edu/api/queue/run/dspaceq.tasks.tasks.dspace_ingest/.json",
        #                    data=dumps(ingest_args), headers=headers)
        #print(req.content)