#!/usr/bin/node
const q = parseInt(process.argv[2]);

if (isNaN(q)) {
    console.log('Missing size');
}
else {
    for (let i = 0; i < q; i++) {
        for (let j = 0; j < q; j++) {
            process.stdout.write('X')
        }
        process.stdout.write('\n');
    }
}
