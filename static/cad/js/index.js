let socket = new WebSocket("ws://127.0.0.1:8000/")

socket.onopen = await function () {
    async function postData(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
      },

      body: JSON.stringify(data)
    })
    return await response.json()
  }
}