export default function setFromArray(array) {
    const set = new Set();
    for (let x of array) {
        set.add(x);
    }
    return set;
}
