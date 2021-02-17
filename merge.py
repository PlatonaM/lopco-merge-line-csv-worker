"""
   Copyright 2021 InfAI (CC SES)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


import os
import uuid
import requests


dep_instance = os.getenv("DEP_INSTANCE")
job_callback_url = os.getenv("JOB_CALLBACK_URL")
delimiter = os.getenv("delimiter")
time_column = os.getenv("time_column")
input_file = os.getenv("input_csv")
data_cache_path = "/data_cache"
output_file = uuid.uuid4().hex


print("merging lines ...")
with open("{}/{}".format(data_cache_path, input_file), "r") as in_file:
    with open("{}/{}".format(data_cache_path, output_file), "w") as out_file:
        first_line = in_file.readline()
        out_file.write(first_line)
        first_line = first_line.strip().split(delimiter)
        time_col_num = first_line.index(time_column)
        current_timestamp = None
        line_count = 1
        for line in in_file:
            line = line.strip()
            line = line.split(delimiter)
            if line[time_col_num] != current_timestamp:
                try:
                    out_file.write(delimiter.join(merge_line) + "\n")
                    line_count += 1
                except NameError:
                    pass
                merge_line = [str()] * len(first_line)
                merge_line[time_col_num] = line[time_col_num]
                current_timestamp = line[time_col_num]
            for pos in range(len(line)):
                if line[pos] and pos != time_col_num:
                    merge_line[pos] = line[pos]
        out_file.write(delimiter.join(merge_line) + "\n")
        line_count += 1

with open("{}/{}".format(data_cache_path, output_file), "r") as file:
    for x in range(5):
        print(file.readline().strip())
print("total number of lines written: {}".format(line_count))

try:
    resp = requests.post(
        job_callback_url,
        json={dep_instance: {"output_csv": output_file}}
    )
    if not resp.ok:
        raise RuntimeError(resp.status_code)
except Exception as ex:
    try:
        os.remove("{}/{}".format(data_cache_path, output_file))
    except Exception:
        pass
    raise ex
