// console.log('this is api scripts....','api.js');



function apiData()  {

  return {
    isLoading: false,
    data: [],

    async fetchApiData() {
      this.isLoading = true;

      const token = 'YOUR_DATABRICKS_API_TOKEN'
      const instance = 'YOUR_DATABRICKS_INSTANCE' // e.g., 'https://<your-instance>.cloud.databricks.com'

        try {
          const response = await fetch(`${instance}/api/2.0/groups/list`, {
            method: 'GET',
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'application/json',
            },
          })

          if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`)
          }

          const data = await response.json()
          this.data = data // Adjust based on API response structure
        } catch (error) {
          console.error('Failed to fetch groups:', error)
        }
      }
    }
}
