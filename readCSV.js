const csv = require('csv-parser');
const fs = require('fs');

let data = [];
fs.createReadStream('data.csv')
  .pipe(csv())
  .on('data', (row) => {
    console.log(row);
    data.push(row);
  })
  .on('end', () => {
    console.log('CSV file successfully processed');
    console.log("I should have all of the data now");
    console.log(JSON.stringify(data));

    for(const obj of data) {
      obj.Float = parseFloat(obj.Float);
      obj.FirstName = obj.FirstName.trim();
      obj.LastName = obj.LastName.trim();
    }
    console.log(JSON.stringify(data));
  });
