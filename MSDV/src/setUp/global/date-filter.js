import moment from 'moment';

export default function dateTime(value) {
    return moment(value).format('DD.MM.YY');
}
