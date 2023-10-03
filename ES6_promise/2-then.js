export default function handleResponseFromAPI(promise) {
  return promise
    .then(promise)
    .catch(Error)
    .finally(console.log('Got a response from the API'))
}
