export default function setFromArray(array) {
  const set = new Set();
  for (const x of array) {
    set.add(x);
  }
  return set;
}
