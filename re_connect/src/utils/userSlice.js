"use client";
import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  user: {},
  isLogedIn: false,
};

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        addUser(state, action) {
            state.user = action.payload;
            state.isLogedIn = true;
        },
        removeUser(state) {
            state.user = null;
            state.isLogedIn = false;
        },
    }
})

export const { addUser, removeUser } = userSlice.actions;
export default userSlice.reducer;