<script lang="ts">
    import { is_expanded } from "../store";
    import SideBarButton from "./SideBarButton.svelte";
    import { page } from '$app/stores'

</script>

<aside class={$is_expanded === 'true' ? 'is_expanded sidebar-wrapper' : 'sidebar-wrapper'}>
    <div class="menu-toggle-wrapper">
        {#if $is_expanded === 'true'}
            <button class="menu-toggle" on:click={() => is_expanded.set('false')}>
                <SideBarButton/>
            </button>
        {:else}
            <button class="menu-toggle" on:click={() => is_expanded.set('true')}>
                <SideBarButton/>
            </button>
        {/if}
    </div>
    <div class="menu">
        <a on:click={() => is_expanded.set('false')} href='/' class={$page.url.pathname === '/' ? "current-route menu-button" : "inactive-route menu-button" }>
            <span class="menu-text">Home</span>
        </a>
        
        <a on:click={() => is_expanded.set('false')} href='/about' class={$page.url.pathname === '/about' ? "current-route menu-button" : "inactive-route menu-button"}>
            <span class="menu-text">About</span>
        </a>
        
        <a on:click={() => is_expanded.set('false')} href='/projects/current' class={$page.url.pathname === '/projects/current' || $page.url.pathname === '/projects/current' ? "current-route menu-button" : "inactive-route menu-button"}>
            <span class="menu-text">Projects</span>
        </a>
        
        <a on:click={() => is_expanded.set('false')} href='/resume' class={$page.url.pathname === '/resume' ? "current-route menu-button" : "inactive-route menu-button"}>
            <span class="menu-text">Resume</span>
        </a>
        
    </div>
</aside>

<style lang="scss">
    aside {
        z-index: 20;
        position: absolute;
        right: 0;
        flex-direction: column;
        width: calc(4rem + 52px);
        overflow: hidden;
        min-height: 100vh;

        // background-color: blueviolet;
        
        transition: 0.2s ease-in-out;
        
        .menu-toggle-wrapper {
            display: flex;
            justify-content: flex-end;
            height: calc(4rem + 52px);;
            
            .menu-toggle {
                transition: 0.2s ease-out;
                padding: 2rem;
            }
        }
        
        .menu {
            display: none;
        }
        
        &.is_expanded {
            width: var(--side-bar-width);
            background-color: var(--dark-background);
            border-left: white 1px solid;
            // backdrop-filter: blur(10px);

            .menu-toggle-wrapper {
                margin-right: auto;
            }

            .menu {
                display: flex;
                flex-direction: column;
                padding: 1rem;

                .menu-button .menu-text {
                    opacity: 1;
                }
    
                .menu-text {
                    visibility: visible;
                    font-size: 2rem;
                }

                .current-route {
                    color: var(--link-active-hover);
                }

                .inactive-route {
                    color: var(--link-inactive)
                }
    
                .menu-button {
                    .material-symbols-outlined {
                        margin-right: 1rem;
                    }
    
                    // &.router-link-exact-active {
                    //     background-image: linear-gradient(to right, var(--light-pink) 50%, var(--dark-aquamarine));
                    // }   
                }
            }
        }

        @media (max-width: 768px) {
            position: fixed;
            z-index: 99;
        }
    }
</style>