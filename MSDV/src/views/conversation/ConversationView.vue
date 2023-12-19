<template>
    <suspense>
        <template #default>
            <div class="flex flex-col justify-center h-[30rem]">
                <div v-for="(chat, index) in chats" :key="index">
                    <div
                        v-if="chat.user.id === currentUser"
                        class="m-2 md:ml-[15%]"
                    >
                        <div class="flex flex-row-reverse items-center">
                            <div
                                class="flex flex-col justify-center items-center"
                            >
                                <div
                                    class="text-slate-400 p-4 rounded-full border border-slate-400 m-3"
                                >
                                    <i class="items-center flex justify-center">
                                        <font-awesome-icon
                                            icon="fa-solid fa-user"
                                        />
                                    </i>
                                </div>
                            </div>
                            <div class="m-2 relative">
                                <div
                                    v-if="!chat.editing"
                                    class="rounded-lg rounded-tr-none shadow-xl border dark:border-none overflow-auto dark:bg-sky-900 bg-sky-700 w-fit px-10 py-1 mt-2"
                                    @click="toggleEdit(chat.id)"
                                >
                                    {{ chat.content }}
                                </div>
                                <textarea
                                    v-else
                                    :ref="`editInput-${index}`"
                                    v-model="textMessage"
                                    class="rounded-lg rounded-tr-none shadow-xl border dark:border-none dark:bg-sky-900 w-full px-10 py-1"
                                    @blur="updateText(chat.id)"
                                    @keydown.enter="updateText(chat.id)"
                                >
                                </textarea>
                                <span class="font-extralight text-xs"
                                    >{{ chat.created_at_formatted }} ago</span
                                >
                                <div
                                    class="md:flex hidden flex-col absolute top-0 rounded-xl space-y-4 bg-sky-700 dark:bg-slate-500 duration-500 ease-in-out overflow-hidden text-xs"
                                    :class="
                                        currentEditIndex === chat.id
                                            ? 'translate-y-0 opacity-100 pointer-events-auto'
                                            : 'translate-y-[-10px] opacity-0 pointer-events-none'
                                    "
                                >
                                    <button
                                        @click="editText(chat, index)"
                                        class="dark:hover:bg-slate-700 hover:bg-sky-800 p-2 rounded-xl"
                                    >
                                        bearbeiten
                                    </button>
                                    <button
                                        @click="removeText(chat.id)"
                                        class="dark:hover:bg-slate-700 hover:bg-sky-800 p-2 rounded-xl"
                                    >
                                        löschen
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-else class="m-5">
                        <div class="flex flex-row items-center relative">
                            <div
                                class="flex flex-col justify-center items-center"
                            >
                                <div
                                    class="text-slate-400 p-4 rounded-full border border-slate-400 m-3"
                                >
                                    <i class="items-center flex justify-center">
                                        <font-awesome-icon
                                            icon="fa-solid fa-user"
                                        />
                                    </i>
                                </div>
                                <div
                                    class="font-extralight text-xs absolute -bottom-1"
                                >
                                    {{ chat.user.username }}
                                </div>
                            </div>
                            <div class="">
                                <div
                                    class="font-extralight mb-1 pr-2 hover:font-light text-xs flex justify-end"
                                >
                                    <span
                                        v-if="!tasksAdded[index]"
                                        class="hover:cursor-pointer border-b border-b-slate-500"
                                        @click="
                                            addTask(chat.content, index);
                                            editTask(index);
                                        "
                                    >
                                        add to Tasks
                                    </span>
                                </div>
                                <div
                                    class="rounded-lg flex flex-col rounded-tl-none shadow-xl border dark:border-none overflow-auto dark:bg-slate-500 w-fit px-10 py-1 dark:text-slate-50 text-slate-900 bg-slate-100"
                                >
                                    {{ chat.content }}
                                </div>
                                <span
                                    class="font-extralight text-xs flex justify-end pr-2"
                                    >{{ chat.created_at_formatted }} ago</span
                                >
                            </div>
                        </div>
                    </div>
                </div>
                <div
                    class="sticky bottom-0 flex flex-row border-t border-t-slate-500 justify-around items-center p-2 dark:bg-slate-600 bg-gray-50 mt-1 py-4 px-3 backdrop-blur"
                >
                    <textarea
                        type="text"
                        @keydown.enter.prevent="send_message"
                        class="shadow-xl w-full p-2 rounded-lg mx-2 dark:bg-slate-500 dark:text-slate-100 text-slate-900"
                        placeholder="write anything"
                        v-model="content"
                    ></textarea>
                    <button
                        @click="send_message"
                        class="px-3 py-2 rounded-full dark:bg-sky-900 text-slate-100 dark:hover:bg-sky-700 bg-sky-700 hover:bg-sky-600"
                    >
                        <font-awesome-icon icon="fa-solid fa-paper-plane" />
                    </button>
                </div>
            </div>
        </template>
        <template #fallback>
            <div>loading ...</div>
        </template>
    </suspense>
</template>
<script>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { useUserStore } from '@/stores/accounts/user';
import { onMounted, reactive, ref } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
    name: 'conversation',
    components: { FontAwesomeIcon },
    setup() {},
    data() {
        return {
            currentEditIndex: null,
            content: '',
            tasksAdded: reactive({}),
            chats: [],
            textMessage: '',
            conversation_id: '',
            patient_id: useRoute().params.id,
            currentUser: useUserStore().user.id
        };
    },
    mounted() {
        this.get_conversation();
        this.loadTasks();
        this.scrollToBottom();
    },
    methods: {
        toggleEdit(index) {
            if (this.currentEditIndex === index) {
                this.currentEditIndex = null;
            } else {
                this.currentEditIndex = index;
            }
        },
        editText(chat, index) {
            this.chats.forEach((c) => {
                if (c !== chat) c.editing = false;
            });
            chat.editing = true;
            this.textMessage = chat.content;
            this.$nextTick(() => {
                this.$refs[`editInput-${index}`][0].focus();
            });
            this.toggleEdit(index);
        },
        updateText(index) {
            axios
                .put(`/api/conversation/${index}/edit/`, {
                    content: this.textMessage,
                    conversation: this.conversation_id
                })
                .then((response) => {
                    let chat = this.chats.find((chat) => chat.id === index);
                    if (chat) {
                        chat.content = this.textMessage;
                        chat.editing = false;
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
            this.toggleEdit(index);
        },
        removeText(index) {
            axios
                .delete(`/api/conversation/${index}/delete/`)
                .then((response) => {
                    this.get_messages();
                })
                .catch((error) => {
                    console.log(error);
                });
            this.toggleEdit(index);
        },
        loadTasks() {
            const tasksAddedStorage = JSON.parse(
                localStorage.getItem('tasksAdded')
            );
            if (tasksAddedStorage) {
                this.tasksAdded = tasksAddedStorage;
            }
        },
        async get_conversation() {
            await axios
                .get(`/api/conversation/${this.patient_id}/`)
                .then((response) => {
                    this.conversation_id = response.data.id;
                    this.get_messages();
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        async send_message() {
            if (this.content !== '') {
                const message = {
                    content: this.content
                };
                await axios
                    .post(
                        `/api/conversation/${this.conversation_id}/message/`,
                        message
                    )
                    .then((response) => {
                        this.content = '';
                        this.get_messages();
                        this.scrollToBottom();
                    })
                    .catch((error) => {
                        console.log(error.response.data);
                    });
            }
        },
        async get_messages() {
            await axios
                .get(`/api/conversation/${this.conversation_id}/messages/`)
                .then((response) => {
                    this.chats = response.data;
                })
                .catch((error) => {
                    console.log(error.response.data);
                });
        },
        addTask(text, num) {
            axios
                .post('api/todo/create/', {
                    name: text,
                    patient: this.patient_id
                })
                .then((response) => {
                    this.tasksAdded[num] = true;
                    this.saveTasks();
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        editTask(num) {
            this.tasksAdded[num] = true;
            this.saveTasks();
        },
        saveTasks() {
            localStorage.setItem('tasksAdded', JSON.stringify(this.tasksAdded));
        },

        scrollToBottom() {
            setTimeout(() => {
                this.$nextTick(() => {
                    let scrollable = document.querySelector('.chatScroll');

                    if (scrollable) {
                        scrollable.scrollTo({
                            top: scrollable.scrollHeight,
                            behavior: 'smooth'
                        });
                    }
                });
            }, 400);
        }
    }
};
</script>
