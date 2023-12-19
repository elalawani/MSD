import { defineStore } from 'pinia';
import axios from 'axios';
import router from '@/router';

export const useMeasurementsStore = defineStore({
    id: 'measurement',

    state: () => ({
        parkinsonMeasurements: [],
        heartRateMeasurements: [],
        bloodGlucoseMeasurement: [],
        bloodPressureMeasurement: [],
        temperatureMeasurement: [],
        respirationRateMeasurement: [],
        bloodCholesterolMeasurement: []
    }),

    actions: {
        async getParkinson(patient_id) {
            this.parkinsonMeasurements = [];
            await axios
                .get(`/api/sensor/parkinson/${patient_id}`)
                .then((response) => {
                    this.parkinsonMeasurements = response.data;
                })
                .catch((error) => {
                    console.log('error', error.response.status);
                    if (error.response && error.response.status === 403) {
                        router.push({ name: 'all_patients' });
                    }
                });
        },
        async getHeartRateMeasurements(patient_id) {
            this.heartRateMeasurements = [];
            await axios
                .get(`/api/sensor/heart_rate/${patient_id}`)
                .then((response) => {
                    this.heartRateMeasurements = response.data;
                })
                .catch((error) => {
                    console.log('error', error.response.status);
                    if (error.response && error.response.status === 403) {
                        router.push({ name: 'all_patients' });
                    }
                });
        },
        async getBloodCholesterolMeasurement(patient_id) {
            this.bloodCholesterolMeasurement = [];
            await axios
                .get(`/api/sensor/blood_cholesterol/${patient_id}`)
                .then((response) => {
                    this.bloodCholesterolMeasurement = response.data;
                })
                .catch((error) => {
                    console.log('error', error.response.status);
                    if (error.response && error.response.status === 403) {
                        router.push({ name: 'all_patients' });
                    }
                });
        },
        async getBloodGlucoseMeasurement(patient_id) {
            this.bloodGlucoseMeasurement = [];
            await axios
                .get(`/api/sensor/blood_glucose/${patient_id}`)
                .then((response) => {
                    this.bloodGlucoseMeasurement = response.data;
                })
                .catch((error) => {
                    console.log('error', error.response.status);
                    if (error.response && error.response.status === 403) {
                        router.push({ name: 'all_patients' });
                    }
                });
        },
        async getBloodPressureMeasurement(patient_id) {
            this.bloodPressureMeasurement = [];
            await axios
                .get(`/api/sensor/blood_pressure/${patient_id}`)
                .then((response) => {
                    this.bloodPressureMeasurement = response.data;
                })
                .catch((error) => {
                    console.log('error', error.response.status);
                    if (error.response && error.response.status === 403) {
                        router.push({ name: 'all_patients' });
                    }
                });
        },
        async getTemperatureMeasurement(patient_id) {
            this.temperatureMeasurement = [];
            await axios
                .get(`/api/sensor/temperature/${patient_id}`)
                .then((response) => {
                    this.temperatureMeasurement = response.data;
                })
                .catch((error) => {
                    console.log('error', error.response.status);
                    if (error.response && error.response.status === 403) {
                        router.push({ name: 'all_patients' });
                    }
                });
        },
        async getRespirationRateMeasurement(patient_id) {
            this.respirationRateMeasurement = [];
            await axios
                .get(`/api/sensor/respiration_rate/${patient_id}`)
                .then((response) => {
                    this.respirationRateMeasurement = response.data;
                })
                .catch((error) => {
                    console.log('error', error.response.status);
                    if (error.response && error.response.status === 403) {
                        router.push({ name: 'all_patients' });
                    }
                });
        }
    }
});
