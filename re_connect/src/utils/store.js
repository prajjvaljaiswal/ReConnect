"use client";
import { configureStore } from '@reduxjs/toolkit';
import userReducer from './userSlice';
// Create the Redux store
export const store = configureStore({
  reducer: {
    // Add your reducers here
    user: userReducer,
  },
});