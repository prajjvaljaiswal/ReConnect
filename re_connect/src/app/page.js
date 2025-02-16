"use client";

import { Provider } from "react-redux";
import { store } from "../utils/store";
import HomePage from "@/components/homePage";


export default function Home() {
  return (
    <Provider store={store}>
      <div>
        <HomePage />
      </div>
    </Provider>
  );
}
