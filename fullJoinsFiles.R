# Load the necessary package
library(tidyverse)

# Get the command line arguments
args <- commandArgs(trailingOnly = TRUE)

# Function to print usage instructions
print_usage <- function() {
  cat("Error: Incorrect input parameters.\n\n")
  cat("Function Description:\n")
  cat("This script is used to perform a full join on multiple files based on a specified column (e.g., geneID).\n")
  cat("You need to provide at least two input file paths, one column name for joining the files, and the last parameter as the output file name.\n\n")
  cat("Correct input format:\n")
  cat("Rscript fullJoinsFiles.R <file1_path> <file2_path> ... <column_name> <output_file_name>\n\n")
  cat("For example: Rscript fullJoinsFiles.R 4kinds_leaf.txt HZ_leaf.txt QFZ_leaf.txt geneID merged_leaf_data.txt\n")
  quit(status = 1)  # Exit the script after printing usage
}

# Check for correct number of arguments
if (length(args) < 3) print_usage()

# Extract file paths, column name, and output file name from arguments
file_paths <- args[1:(length(args)-2)]
column_name <- args[length(args)-1]
output_file <- args[length(args)]

# Check if all files exist
missing_files <- file_paths[!file.exists(file_paths)]
if (length(missing_files) > 0) {
  cat("Error: Unable to read the following file(s):\n")
  cat(paste(missing_files, collapse = "\n"), "\n")
  quit(status = 1)  # Exit if files are missing
}

# Read the first file
merged_data <- read_tsv(file_paths[1])

# Perform full joins with the remaining files
for (file in file_paths[-1]) {
  current_file <- read_tsv(file)

  # Check if the column exists in the current file
  if (!(column_name %in% colnames(current_file))) {
    cat(paste("Error: The specified column", column_name, "was not found in file", file, ". Please ensure the column name is correct and exists in the file.\n"))
    quit(status = 1)  # Exit if column is missing
  }

  merged_data <- merged_data %>% full_join(current_file, by = column_name)
}

# Preview the merged data
head(merged_data)

# Write the merged data to the output file
write_tsv(merged_data, output_file)

# Notify user about the saved file
cat("The merged data has been saved to", output_file, "\n")
