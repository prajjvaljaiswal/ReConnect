"use client";
import { useEffect, useState } from "react";

export default useUser = (email) => {
    const baseUrl = "http://127.0.0.1:8000";
    const [user, setUser] = useState(null);

    useEffect(() => {
        const fetchUser = async () => {
            try {
                const response = await fetch(baseUrl + "/user/"+email);
                const data = await response.json();
                setUser(data);
            } catch (error) {
                console.error("Failed to fetch user", error);
            }
        };

        fetchUser();
    }, []);

    return user;
};