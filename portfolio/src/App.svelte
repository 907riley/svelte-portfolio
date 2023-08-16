<script lang="ts">
    import { Router, Link, Route } from 'svelte-routing'

    import NavBar from "./NavBar.svelte";
    import Projects from './pages/Projects.svelte';
    import Resume from './pages/Resume.svelte';
    import About from './pages/About.svelte';
    import Home from './pages/Home.svelte';

    export let url = '/'
</script>

<Router {url}>
    <main>
        <NavBar/>
        <Route path='/projects'><Projects/></Route>
        <Route path='/resume'><Resume/></Route>
        <Route path='/about'><About/></Route>
        <Route path='/'><Home/></Route>
    </main>
</Router>

<style lang="scss">
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
