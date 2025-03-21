# MOTOR MEDS

> [!WARNING]
> This code is not yet viable; FEMR requires an older version of MEDS which is not compatible with MEDS-DEV.


A MEDS / MEDS-DEV compatible runner for the MOTOR model. To use the MOTOR model, you need to follow the
following steps:

## Step 0: Dataset Needs
  1. Raw Data: You need to have a dataset in the
     [MEDS format](https://medical-event-data-standard.github.io/), stored on disk in the `$RAW_DATASET_DIR`
     folder.
  2. Task Labels: You need to have prediction task labels specified in the MEDS label format, stored on disk
     in the `$TASK_LABELS` folder. All `.parquet` files in any recursive level of subdirectory within that
     folder will be assumed to be a label file.

## Step 1: Installation
```bash
pip install motor-meds
pip install git+https://github.com/som-shahlab/femr@meds_v3
```

## Step 2: Download the ATHENA files

In addition to installing this module, you also need to download the ATHENA vocabulary files. To do so, follow
these setps:
  1. Go to the [Athena website](https://athena.ohdsi.org/)
  2. If necessary, make an account or sign in to your existing account.
  3. Navigate to the ["Download" tab](https://athena.ohdsi.org/vocabulary/list)
  4. Click on the checkbox in the upper left to indicate you want all vocabularies.
  5. Click on the "Download Vocabularies" button in the upper right.
  6. Fill out the "name bundle" field in the form.
  7. Scroll to the bottom of the page and click on the download button.
  8. Wait until you receive an email indicating the download has been prepared.
  9. Download the resulting file. It should be a zip file of about 1.2G

After you have downloaded the file, unzip it into a folder on disk that you assign to environment
variable `$ATHENA_DOWNLOAD_DIR`. This folder should have around 7.1G of files in it (less 1.2G if you delete
the original zip file) and should contain a collection of `.csv`, `.jar`, `.bat`, `.sh`, `.txt`, and the
original `.zip` file in it.

## Step 3. Pre-process the data
Designate a directory to store the MEDS-Reader converted data. Call it `$MEDS_READER_DIR`. Then

```bash
meds_reader_convert $RAW_DATASET_DIR $MEDS_READER_DIR
```

## Step 4. Pre-train MOTOR

Designate a directory to store the processed pre-training data. Call it `$PROCESSED_PRETRAINING_DATA_DIR`.
Then

```bash
python -u -m femr.omop_meds_tutorial.prepare_motor \
  --pretraining_data $PROCESSED_PRETRAINING_DATA_DIR \
  --athena_path $ATHENA_DOWNLOAD_DIR \
  --meds_reader $MEDS_READER_DIR

python -u -m femr.omop_meds_tutorial.pretrain_motor \
  --pretraining_data $PROCESSED_PRETRAINING_DATA_DIR \
  --meds_reader $MEDS_READER_DIR
```

## Step 5. Fine-tune MOTOR
???

This trains a logistic regression model over MOTOR embeddings; it doesn't fine-tune the whole model. It also
requires you to copy a file manually in a step not specified here.
```bash
python -u -m femr.omop_meds_tutorial.generate_motor_features \ 
  --pretraining_data $PROCESSED_PRETRAINING_DATA_DIR \
  --meds_reader $MEDS_READER_DIR

python -u -m femr.omop_meds_tutorial.finetune_motor \
  --pretraining_data $PROCESSED_PRETRAINING_DATA_DIR \
  --meds_reader $MEDS_READER_DIR
```
