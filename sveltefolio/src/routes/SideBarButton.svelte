<div class="triple-bar-wrapper">
    <svg xmlns="http://www.w3.org/2000/svg" width="52" height="5" viewBox="0 0 52 5" fill="none">
        <path d="M2.66669 2.66666H49.3334" stroke="black" stroke-width="4" stroke-linecap="round"/>
    </svg>
    <svg xmlns="http://www.w3.org/2000/svg" width="52" height="5" viewBox="0 0 52 5" fill="none">
        <path d="M2.66669 2.66666H49.3334" stroke="black" stroke-width="4" stroke-linecap="round"/>
    </svg>
    <svg xmlns="http://www.w3.org/2000/svg" width="52" height="5" viewBox="0 0 52 5" fill="none">
        <path d="M2.66669 2.66666H49.3334" stroke="black" stroke-width="4" stroke-linecap="round"/>
    </svg>
</div>

<style lang="scss">
    .triple-bar-wrapper {
        display: grid;
        grid-template-rows: repeat(3, minmax(0, 1fr));
        gap: 0.75rem;
        margin-left: auto;
        margin-right: auto;

        svg {
            path {
                stroke: var(--link-active-hover);
            }
        }

        &:hover {
            svg {
                path {
                    transition: 0.2s ease-out;
                    stroke: var(--link-active-hover);
                }
            }   
        }
    }
</style>