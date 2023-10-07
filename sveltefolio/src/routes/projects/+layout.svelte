<script lang="ts">
    import { page } from '$app/stores'

</script>


<main>
    <nav class="nav-container">
        <div class="button-wrapper-inner">
            <div class="nav-button-wrapper-inner">
                <a href='/projects/current' class={$page.url.pathname === '/projects/current' ? "current-route" : "inactive-route" }>Current</a>
            </div>
            <div class="nav-button-wrapper-inner">
                <a href='/projects/past' class={$page.url.pathname === '/projects/past' ? "current-route" : "inactive-route"}>Past</a>
            </div>
    </nav>
    <slot/>
</main>

<style lang="scss">
    .nav-container {
        display: flex;
        width: 100%;
        flex-direction: column;   
        align-items: center;
        .button-wrapper-inner {
            display: flex;
            width: 50%;
            flex-direction: row;   
            justify-content: center;  
            .nav-button-wrapper-inner {
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