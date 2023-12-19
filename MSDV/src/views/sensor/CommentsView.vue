<template>
    <div>
        <div v-if="isLoading">Loading...</div>
        <div v-else class="text-slate-900 dark:text-slate-50">
            <form>
                <div class="w-full mb-4 rounded-lg">
                    <div
                        class="px-4 m-2 py-2 rounded-lg dark:bg-gray-800 shadow"
                    >
                        <textarea
                            v-model="form.text"
                            class="w-full p-2 border dark:border-slate-700 dark:bg-slate-800 dark:placeholder-slate-400"
                            placeholder="Ihr Kommentar..."
                        >
                        </textarea>
                        <div v-if="errors.name" class="ml-4 text-red-500">
                            {{ errors.name }}
                        </div>
                    </div>
                    <div class="flex items-center justify-between px-3 py-2">
                        <button
                            type="submit"
                            class="inline-flex items-center py-3 px-4 text-center text-white dark:bg-sky-700 rounded-lg dark:hover:bg-sky-800 bg-sky-600 hover:bg-sky-700"
                            @click.prevent="submitForm"
                        >
                            absenden
                        </button>
                    </div>
                </div>
            </form>
            <div
                v-if="commentStore.comments.length"
                class="m-2 max-h-96 overflow-auto"
            >
                <span>Kommentare</span>

                <div
                    v-for="(comments, index) in commentStore.comments"
                    :key="index"
                    class="p-2 mt-5 flex flex-col w-full shadow-lg dark:bg-slate-700 justify-center rounded-lg"
                >
                    <div>Kommentar von: {{ comments.user.username }}</div>
                    <div class="p-2">
                        {{ comments.text }}
                    </div>
                    <div class="text-xs font-light">
                        am: {{ dateTime(comments.created_at) }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useCommentsStore } from '@/stores/sensor/comments';
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import dateTime from '../../setUp/global/date-filter';

let props = defineProps({
    measurementId: {
        type: Number,
        required: true
    }
});

let form = {
    text: '',
    measurement: props.measurementId
};

let errors = ref({ name: '' });
let patient_id = useRoute().params.id;
let comment = useCommentsStore();

const submitForm = async () => {
    errors.value.name = '';
    if (form.text === '') {
        errors.value.name = 'kann keine leere inhalt kommentiert werden';
    }

    if (errors.value.name === '') {
        const newComment = await comment.creatComment(form);
        if (newComment) {
            commentStore.comments.unshift(newComment);
        }
    }
    form.text = '';
};

// get comments

const commentStore = useCommentsStore();
const isLoading = ref(true);
const fetchError = ref(null);

const fetchComments = async (patient_id) => {
    isLoading.value = true;
    try {
        await commentStore.getComment(patient_id);
    } catch (e) {
        console.log(e);
    }

    isLoading.value = false;
};

fetchComments(patient_id);
</script>
