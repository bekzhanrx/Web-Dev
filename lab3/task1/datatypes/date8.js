'use strict'

function formatDate(date) {
    let dayOfMonth = date.getDay();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();
    let hour = date.getHours();
    let minutes = date.getMinutes();
    let diffMs = new Date() - date;
    let diffSec = Math.round(diffMs / 1000);
    let diffMin = diffSec / 60;
    let diffHour = diffMin / 60;

    if (diffSec < 1) {
        return 'right now';
      } else if (diffMin < 1) {
        return `${diffSec} sec. ago`
      } else if (diffHour < 1) {
        return `${diffMin} min. ago`
      } else {
        return `${dayOfMonth}.${month}.${year} ${hour}:${minutes}`
      }
}


console.log(formatDate(formatDate(new Date(new Date - 86400 * 1000))));