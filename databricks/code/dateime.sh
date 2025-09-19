az datafactory pipeline-run show \
  --factory-name <your-adf-name> \
  --resource-group <your-rg> \
  --run-id <pipeline-run-id> -o json \
| jq -r '"\(.pipelineName) \(.runStart) \(.runEnd) \(.durationInMs)"' \
| while read name start end duration; do
    start_est=$(TZ="America/New_York" date -d "$start" +"%Y-%m-%d %H:%M:%S %Z")
    end_est=$(TZ="America/New_York" date -d "$end" +"%Y-%m-%d %H:%M:%S %Z")
    dur_fmt="$((duration/1000/3600))h $(((duration/1000%3600)/60))m $((duration/1000%60))s"
    echo "$name | $start_est | $end_est | $dur_fmt"
  done



#!/bin/bash

# Variables
ADF_NAME="<your-adf-name>"
RG_NAME="<your-rg>"
TRIGGER_NAME="<trigger-name>"
TRIGGER_RUN_ID="<your-trigger-run-id>"
TO_EMAIL="recipient@example.com"
SUBJECT="ADF Trigger Run Pipeline Report"
OUTPUT_FILE="/tmp/adf_pipeline_report.html"

# Create HTML header
cat <<EOF > "$OUTPUT_FILE"
<html>
<head>
<style>
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid black; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }
</style>
</head>
<body>
<h2>ADF Trigger Run Pipeline Report</h2>
<table>
<tr>
<th>Pipeline Name</th>
<th>Start (EST)</th>
<th>End (EST)</th>
<th>Duration</th>
</tr>
EOF

# Generate report rows
az datafactory trigger-run query-by-run \
  --factory-name "$ADF_NAME" \
  --resource-group "$RG_NAME" \
  --trigger-name "$TRIGGER_NAME" \
  --run-id "$TRIGGER_RUN_ID" -o json \
| jq -r '.value[0].properties.TriggeredPipelines[] | "\(.PipelineName) \t \(.PipelineRunId)"' \
| while read name runid; do
    read start end duration <<<$(az datafactory pipeline-run show \
      --factory-name "$ADF_NAME" \
      --resource-group "$RG_NAME" \
      --run-id "$runid" \
      | jq -r '"\(.runStart) \(.runEnd) \(.durationInMs)"')
    # Convert UTC → EST
    start_est=$(TZ="America/New_York" date -d "$start" +"%Y-%m-%d %H:%M:%S %Z")
    end_est=$(TZ="America/New_York" date -d "$end" +"%Y-%m-%d %H:%M:%S %Z")
    dur_fmt="$((duration/1000/3600))h $(((duration/1000%3600)/60))m $((duration/1000%60))s"
    # Append row to HTML table
    echo "<tr><td>$name</td><td>$start_est</td><td>$end_est</td><td>$dur_fmt</td></tr>" >> "$OUTPUT_FILE"
done

# Close HTML
echo "</table></body></html>" >> "$OUTPUT_FILE"

# Send email with HTML content
mailx -a "Content-Type: text/html" -s "$SUBJECT" "$TO_EMAIL" < "$OUTPUT_FILE"
