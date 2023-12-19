<template>
    <div class="flex flex-row items-center justify-around">
        <div class="p-6">
            <div class="text-3xl">Bewertung</div>
            <div class="mb-4 mt-5 flex flex-row justify-between">
                <label class="p-2 font-bold" for="status">
                    patient Status</label
                >
                <span class="text-black">
                    <select
                        class="px-3 py-2 rounded-lg"
                        v-model="status"
                        name="status"
                        id="status"
                    >
                        <option
                            v-for="option in options"
                            :key="option"
                            :value="option"
                        >
                            {{ option }}
                        </option>
                    </select>
                </span>
            </div>
            <div>
                <label class="p-2 font-bold" for="movement">
                    patient Bewegung
                </label>
                <span class="text-black">
                    <select
                        class="px-3 py-2 rounded-lg"
                        v-model="movement"
                        name="movement"
                        id="movement"
                    >
                        <option
                            v-for="option in options"
                            :key="option"
                            :value="option"
                        >
                            {{ option }}
                        </option>
                    </select>
                </span>
            </div>
        </div>
        <div class="mb-16 mt-20 space-y-2 flex flex-col items-center">
            <label
                class="text-sm font-medium text-gray-900 dark:text-white"
                for="file_input"
            >
                json-file hochladen
            </label>
            <input
                class="text-sm text-slate-700 border border-slate-500 rounded-lg cursor-pointer bg-gray-50 dark:text-slate-300 focus:outline-none dark:bg-slate-500 dark:border-slate-600 dark:placeholder-gray-400"
                aria-describedby="file_input_help"
                id="file_input"
                type="file"
                ref="fileInput"
                @change="handleFileUpload"
            />
            <button
                class="py-2 px-4 bg-sky-700 rounded text-white"
                @click="uploadFile"
                :disabled="isLoading"
            >
                hochladen
            </button>
            <div v-if="isLoading" class="spinner"></div>
            <div
                v-if="error"
                class="text-red-900 p-2 border border-red-900 rounded-lg bg-red-50 shadow-xl mt-2"
            >
                {{ error }}
                <span
                    class="text-red-800 font-extralight m-2 hover:cursor-pointer hover:font-light text-xs"
                    @click="showMoreErrorDetails"
                >
                    mehr...
                </span>
            </div>
            <div v-if="errorDetails">
                {{ moreErrorDetails }}
            </div>
        </div>
    </div>
</template>

<style scoped>
.spinner {
    border: 4px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    border-top: 4px solid #000;
    width: 24px;
    height: 24px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}
</style>

<script>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { useToastStore } from '@/stores/toast';

export default {
    name: 'upload',
    setup() {
        const toast = useToastStore();

        return {
            toast
        };
    },
    data() {
        return {
            id: useRoute().params.id,
            selectedFile: null,
            isLoading: false,
            error: null,
            moreErrorDetails: null,
            errorDetails: false,
            status: 1,
            movement: 1,
            options: [1, 2, 3, 4, 5]
        };
    },
    methods: {
        async uploadFile() {
            this.error = null;
            this.isLoading = true;

            const formData = new FormData();
            formData.append('file', this.selectedFile);
            formData.append('patient', this.id);
            formData.append('status', this.status);
            formData.append('movement', this.movement);

            try {
                await axios.post(
                    '/api/measure_fhir/upload_measurement/',
                    formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }
                );
                this.toast.showToast(
                    5000,
                    'Datei erfolgreich hochgeladen',
                    'border border-green-500 bg-green-100 text-green-900'
                );
            } catch (error) {
                console.log(error.response);
                if (error.response && error.response.data) {
                    this.error =
                        error.response.data.error ||
                        'Ein unbekannter Fehler ist aufgetreten.';
                    this.moreErrorDetails = error.response.data.details;
                } else {
                    this.error = 'Beim Hochladen ist ein Fehler aufgetreten.';
                }
                console.log(error);
            } finally {
                this.isLoading = false;
            }
        },
        handleFileUpload() {
            this.selectedFile = this.$refs.fileInput.files[0];
        },
        showMoreErrorDetails() {
            this.errorDetails = !this.errorDetails;
        }
    }
};
</script>
