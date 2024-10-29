// console.log('this is api scripts....','api.js');



function apiData()  {

  return {
    isLoading: false,
    data: [],
    async fetchApiData() {
      this.isLoading = true;

      try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts');
        const data = await response.json();
        this.data = data;
        this.isLoading = false;
      }
      catch (error) {
      this.error = error;
      this.isLoading = false;
      }
    }
  }
}
