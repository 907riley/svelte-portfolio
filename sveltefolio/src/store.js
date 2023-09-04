import { writable } from "svelte/store";
import { browser } from "$app/environment";

export const is_expanded = writable(browser && localStorage.getItem("expanded") || 'false')
is_expanded.subscribe(value => {
    if (browser) {
        localStorage.setItem("expanded", value === 'true' ? 'true' : 'false' )
    }
})