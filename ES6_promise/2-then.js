export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => promise.resolve({ status: 200, body: 'success' }))
    .catch(() => Error())
    .finally(() => console.log('Got a response from the API'));
}
