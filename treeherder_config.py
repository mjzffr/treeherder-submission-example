import os

TREEHERDER_CONFIG = os.environ.get('TREEHERDER_CONFIG') or 'example-credentials'

config = {
    "treeherder_url": "http://local.treeherder.mozilla.org",

    "treeherder_credentials_path": os.path.join(TREEHERDER_CONFIG, "treeherder-local-credentials.json"),
    "s3_credentials_path": os.path.join(TREEHERDER_CONFIG, "s3-credentials.json"),
    "group_name": "Test Group Name",
    "group_symbol": "TGN1",
    "job_name": "Test Job Name",
    "job_symbol": "t",

    # See https://github.com/mozilla/treeherder/blob/master/treeherder/model/sample_data/job_data.json.sample
    "job_description": ("Example treeherder submission"),
    "job_reason": "scheduled",
    "job_who": "xyz"
}
