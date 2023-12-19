import { defineStore } from 'pinia';
import axios from 'axios';

export const useTodolistStore = defineStore({
    id: 'todolist',
    state: () => ({
        tasks: []
    }),
    actions: {
        async getTasks() {
            this.tasks = [];
            await axios
                .get('api/todo/')
                .then((response) => {
                    this.tasks = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    }
});
