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
cat <<EOF > /tmp/adf_pipeline_report.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>ADF Trigger Run Pipeline Report</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Roboto', Arial, sans-serif;
      background-color: #f8f9fa;
      color: #333;
      padding: 20px;
    }
    h2 {
      font-weight: 500;
      color: #2c3e50;
    }
    table {
      border-collapse: collapse;
      width: 100%;
      margin-top: 15px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      background: #fff;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 10px 14px;
      text-align: left;
    }
    th {
      background-color: #007acc;
      color: white;
      font-weight: 500;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <h2>ADF Trigger Run Pipeline Report</h2>
  <table>
    <tr>
      <th>Pipeline Name</th>
      <th>Start Time (EST)</th>
      <th>End Time (EST)</th>
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
