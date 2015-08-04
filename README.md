This is code I played around with to understand how Treeherder submission works. `jenkinsherder.py` is the WebRTC test runner from https://github.com/sydvicious/mozplatformqa-jenkins, but with all the WebRTC stuff stubbed out.

# Setup
* Clone the repo
* Install the requirements in a virtual env (see `requirements.txt`).
* If you have your Treeherder config right (`treeherder_credentials_path`, `s3_credentials_path`, `treeherder_url`), then running `python jenkinsherder.py` should submit some dummy data to whatever Treeherder server you specify. It will also upload the files in `logs` to the S3 bucket you specify.

# References
Treeherder resources:
* Set up a local server: http://treeherder.readthedocs.org/en/latest/installation.html
* Getting local credentials: http://treeherder.readthedocs.org/en/latest/common_tasks.html#look-up-credentials-for-a-project
* Submitting data: http://treeherder.readthedocs.org/en/latest/submitting_data.html

`treeherding.py` and `s3.py` are largely inspired by https://github.com/mozilla/autophone

They are also in use here:
* https://github.com/sydvicious/mozplatformqa-jenkins
* https://github.com/mjzffr/firefox-media-tests/tree/pf-jenkins
* https://github.com/mozilla/mozmill-ci/tree/0c53446fe0a24794303339b688a67ccf3a91d8db
