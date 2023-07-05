import os


def get_file_format_logo_path(instance, filename):
    return os.path.join(
        "fileFormat", "%s" % instance.name, filename
    )


def get_dataset_file_path(instance, filename):
    return os.path.join(
        "Datasets", "%s" % instance.title, filename
    )