import Multiselect from '@vueform/multiselect';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default function registerGlobalComponents(app) {
    app.component('font-awesome-icon', FontAwesomeIcon);
    app.component('multi-select', Multiselect);
}
