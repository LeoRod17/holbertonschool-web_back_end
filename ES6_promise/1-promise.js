export default function getFullResponseFromAPI(success) {
  return new Promise(function (comp, fail) {
    if (success) {
      comp({ status: 200, body: 'Success' });
    }
    fail(Error('The fake API is not working currently'));
  });
}
