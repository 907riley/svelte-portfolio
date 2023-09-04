<script lang="ts">
    import { page } from '$app/stores'
    import Boat from './Boat.svelte';
    import SideBar from './SideBar.svelte';
    import '../app.css'

    const boatImages = {
        resting: "fisherman_static.gif",
        pullback: 'fisherman_pullback.gif',
        cast: 'fisherman_cast.gif'
    }
</script>

<main>
    <nav class="nav-container">
        <div class="button-wrapper">
            <div class="nav-button-wrapper">
                <a href='/' class={$page.url.pathname === '/' ? "current-route" : "inactive-route" }>Home</a>
            </div>
            <div class="nav-button-wrapper">
                <a href='/about' class={$page.url.pathname === '/about' ? "current-route" : "inactive-route"}>About</a>
            </div>
            <div class="nav-button-wrapper">
                <a href='/projects' class={$page.url.pathname === '/projects' ? "current-route" : "inactive-route"}>Projects</a>
            </div>
            <div class="nav-button-wrapper">
                <a href='/resume' class={$page.url.pathname === '/resume' ? "current-route" : "inactive-route"}>Resume</a>
            </div>
        </div>
        <Boat boatImg={boatImages.resting}/>
    </nav>
    <SideBar/>
    <slot/>
</main>

<style lang="scss">
    .nav-container {
        display: flex;
        width: 100%;
        flex-direction: column;   
        align-items: center;
        .button-wrapper {
            width: 50%;
            flex-direction: row;   
            justify-content: center;  
            .nav-button-wrapper {
                margin: .5rem;
                z-index: 10;
                font-weight: bold;
                display: flex;
                justify-content: center;
                flex: auto;
                a {
                    font-size: 1.5rem;
                    text-decoration: none;
                }

                .current-route {
                    color: var(--link-active-hover)
                }
            }
        }
    }

    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100vw;
        height: 100vh;
    }
</style>
