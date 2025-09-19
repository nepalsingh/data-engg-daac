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
