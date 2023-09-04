<script lang="ts">
    import { onMount } from "svelte";

    export let boatImg: string = "fisherman_static.gif"
    let mousePosition: {x: number, y: number} = { x: 0, y: 0 }


    onMount(() => {
        window.addEventListener('mousemove', (event) => {
            mousePosition.x = event.clientX
            mousePosition.y = event.clientY

            let fisherman = document.getElementById("fisherman")
            if (fisherman) {
                let fishermanWidth = fisherman.offsetWidth
                fisherman.style.setProperty('left', (mousePosition.x - fishermanWidth/2) + 'px')
            }
        })
    })

</script>

<!-- This is strictly for a mouse -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div class="fisherman-wrapper">
    <img id="fisherman" src={boatImg} alt="fisherman on a boat"/>
</div>

<style lang="scss">
    .fisherman-wrapper {
        height: 4rem;
    }

    #fisherman {
        width: 6rem;
        position: absolute;
    }

</style>