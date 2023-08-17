<script lang="ts">
    import { Link } from "svelte-routing";
</script>

<nav class="nav-container">
    clouds live here
    <ul class="button-wrapper">
        <li class="nav-button-wrapper">
            <Link to='/'>Home</Link>
        </li>
        <li class="nav-button-wrapper">
            <Link to='/about'>About</Link>
        </li>
        <li class="nav-button-wrapper">
            <Link to='/projects'>Projects</Link>
        </li>
        <li class="nav-button-wrapper">
            <Link to='/resume'>Resume</Link>
        </li>
    </ul>
</nav>

<style lang="scss">
    .button-wrapper {
        list-style: none;
        display: flex;
        flex-direction: row;
        justify-content: center;
        justify-content: space-evenly;

        .nav-button-wrapper {
            margin: 1rem;
            z-index: 10;
            flex: none;
        }
    }
</style>