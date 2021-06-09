## lopco-merge-line-csv-worker

Merge the rows of a CSV file based on the contained timestamps. The CSV file must have been sorted beforehand.

### Configuration

`delimiter`: Delimiter used in the CSV file.

`time_column`: Name of column containing timestamps.

### Inputs

Type: single

`input_csv`: CSV file to sort.

### Outputs

Type: single

`output_csv`: Sorted CSV file.

### Description

    {
        "name": "Merge Line CSV",
        "image": "platonam/lopco-merge-line-csv-worker:latest",
        "data_cache_path": "/data_cache",
        "description": "Merge lines of a Comma-Separated Values file.",
        "configs": {
            "delimiter": null,
            "time_column": null
        },
        "input": {
            "type": "single",
            "fields": [
                {
                    "name": "input_csv",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        },
        "output": {
            "type": "single",
            "fields": [
                {
                    "name": "output_csv",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        }
    }