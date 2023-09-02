<script lang="ts">
    import { link } from "svelte-routing";
    import Boat from "./Boat.svelte";
    import { onMount } from "svelte";

    const boatImages = {
        resting: "fisherman_static.gif",
        pullback: 'fisherman_pullback.gif',
        cast: 'fisherman_cast.gif'
    }

</script>

<nav class="nav-container">
    <ul class="button-wrapper">
        <li class="nav-button-wrapper">
            <a href='/' class="nav-button" use:link>Home</a>
        </li>
        <li class="nav-button-wrapper">
            <a href='/about' class="nav-button" use:link>About</a>
        </li>
        <li class="nav-button-wrapper">
            <a href='/projects' class="nav-button" use:link>Projects</a>
        </li>
        <li class="nav-button-wrapper">
            <a href='/resume' class="nav-button" use:link>Resume</a>
        </li>
    </ul>
    <Boat boatImg={boatImages.resting}/>
</nav>

<style lang="scss">

    .nav-container {
        display: flex;
        width: 100%;
        flex-direction: column;
        .button-wrapper {
            margin: 0;
            padding: 0;
            list-style: none;
            display: flex;
            flex-direction: row;
            justify-content: center;
            
            .nav-button-wrapper {
                margin: 1rem;
                z-index: 10;
                font-weight: bold;
                .nav-button {
                    text-decoration: none;
                }
            }
        }
    }
</style>