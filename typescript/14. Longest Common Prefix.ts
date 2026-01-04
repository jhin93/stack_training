function longestCommonPrefix(strs: string[]): string {
    if (!strs.length) return "";

    strs.sort();

    let firstArr: string[] = strs[0].split('');
    let lastArr: string[] = strs[strs.length - 1].split('');

    let result = "";

    for (let i = 0; i < firstArr.length; i++) {
        if (firstArr[i] === lastArr[i]) {
            result += firstArr[i];
        } else {
            break;
        }
    }
    return result;
}

// test