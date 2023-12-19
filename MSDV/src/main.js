// css Imports
import './assets/main.css';
import '@vueform/multiselect/themes/default.css';

// vue Imports
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// pinia imports
import { createPinia } from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate';

// axios
import axios from 'axios';
import './errors/handle-login-error';

// Global Components
import registerGlobalComponents from '@/setUp/global/global-components';

// fontawesome
import setupFontawesome from '@/setUp/fontawesome/fontawesome-setup';

// configure axios
const baseURL =
    window.location.protocol + '//' + window.location.hostname + ':8000';
axios.defaults.baseURL = baseURL;

// Initialize Pinia and register plugin
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

// Initialize Vue app
const app = createApp(App);

app.use(pinia);
app.use(router, axios);

// Register global components
registerGlobalComponents(app);

// Set up FontAwesome
setupFontawesome();

app.mount('#app');
