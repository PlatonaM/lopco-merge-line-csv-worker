#### Description

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