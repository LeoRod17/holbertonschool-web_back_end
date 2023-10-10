export default function hasValuesFromArray(set, array) {
    for (const x of array) {
        let flag = set.has(x);
        if (flag == false) {
            return false;
        }
    }
    return true;
}
