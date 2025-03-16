<template>
  <div class="col-xl-6">
    <div class="card">
      <div class="card-body card-buttons">
        <h4 class="header-title">Offcanvas Placement</h4>
        <ul class="ps-0 mb-3">
          <li>
            <code>.offcanvas-start</code> places offcanvas on the left of the viewport
            (shown above)
          </li>
          <li>
            <code>.offcanvas-end</code> places offcanvas on the right of the viewport
          </li>
          <li><code>.offcanvas-top</code> places offcanvas on the top of the viewport</li>
          <li>
            <code>.offcanvas-bottom</code> places offcanvas on the bottom of the viewport
          </li>
        </ul>

        <div>
          <div class="button-list">
            <b-button
              variant="primary mt-2 me-1"
              type="button"
              data-bs-toggle="offcanvas"
              data-bs-target="#offcanvasTop"
              aria-controls="offcanvasTop"
            >
              Toggle Top offcanvas
            </b-button>
            <b-button
              variant="primary mt-2 me-1"
              type="button"
              data-bs-toggle="offcanvas"
              data-bs-target="#offcanvasRight"
              aria-controls="offcanvasRight"
            >
              Toggle right offcanvas
            </b-button>
            <b-button
              variant="primary mt-2 me-1"
              data-bs-toggle="offcanvas"
              data-bs-target="#offcanvasBottom"
              aria-controls="offcanvasBottom"
            >
              Toggle bottom offcanvas
            </b-button>
            <b-button
              variant="primary mt-2"
              data-bs-toggle="offcanvas"
              data-bs-target="#offcanvasLeft"
              aria-controls="offcanvasLeft"
            >
              Toggle Left offcanvas
            </b-button>
          </div>
          <!-- end button-list-->

          <div
            class="offcanvas offcanvas-top"
            tabindex="-1"
            id="offcanvasTop"
            aria-labelledby="offcanvasTopLabel"
          >
            <div class="offcanvas-header">
              <h5 id="offcanvasTopLabel">Offcanvas Top</h5>
              <b-button
                type="button"
                class="btn-close text-reset"
                data-bs-dismiss="offcanvas"
                aria-label="Close"
              ></b-button>
            </div>
            <!-- end offcanvas-header-->

            <div class="offcanvas-body">
              <div>
                Some text as placeholder. In real life you can have the elements you have
                chosen. Like, text, images, lists, etc.
              </div>
              <h5 class="mt-3">List</h5>
              <ul class="ps-3">
                <li >Nemo enim ipsam voluptatem quia aspernatur</li>
                <li >Neque porro quisquam est, qui dolorem</li>
                <li >Quis autem vel eum iure qui in ea</li>
              </ul>
            </div>
            <!-- end offcanvas-body-->
          </div>
          <!-- end offcanvas-->

          <div
            class="offcanvas offcanvas-end"
            tabindex="-1"
            id="offcanvasRight"
            aria-labelledby="offcanvasRightLabel"
          >
            <div class="offcanvas-header">
              <h5 id="offcanvasRightLabel">Offcanvas right</h5>
              <b-button
                type="button"
                class="btn-close text-reset"
                data-bs-dismiss="offcanvas"
                aria-label="Close"
              ></b-button>
            </div>
            <!-- end offcanvas-header-->

            <div class="offcanvas-body">
              <div>
                Some text as placeholder. In real life you can have the elements you have
                chosen. Like, text, images, lists, etc.
              </div>
              <h5 class="mt-3">List</h5>
              <ul class="ps-3">
                <li >Nemo enim ipsam voluptatem quia aspernatur</li>
                <li >Neque porro quisquam est, qui dolorem</li>
                <li >Quis autem vel eum iure qui in ea</li>
              </ul>
            </div>
            <!-- end offcanvas-body-->
          </div>
          <!-- end offcanvas-->

          <div
            class="offcanvas offcanvas-bottom"
            tabindex="-1"
            id="offcanvasBottom"
            aria-labelledby="offcanvasBottomLabel"
          >
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="offcanvasBottomLabel">Offcanvas bottom</h5>
              <b-button
                type="button"
                class="btn-close text-reset"
                data-bs-dismiss="offcanvas"
                aria-label="Close"
              ></b-button>
            </div>
            <!-- end offcanvas-header-->

            <div class="offcanvas-body">
              <div>
                Some text as placeholder. In real life you can have the elements you have
                chosen. Like, text, images, lists, etc.
              </div>
              <h5 class="mt-3">List</h5>
              <ul class="ps-3">
                <li >Nemo enim ipsam voluptatem quia aspernatur</li>
                <li >Neque porro quisquam est, qui dolorem</li>
                <li >Quis autem vel eum iure qui in ea</li>
              </ul>
            </div>
            <!-- end offcanvas-body-->
          </div>
          <!-- end offcanvas-->

          <div
            class="offcanvas offcanvas-start"
            tabindex="-1"
            id="offcanvasLeft"
            aria-labelledby="offcanvasLeftLabel"
          >
            <div class="offcanvas-header">
              <h5 id="offcanvasLeftLabel">Offcanvas Left</h5>
              <b-button
                type="button"
                class="btn-close text-reset"
                data-bs-dismiss="offcanvas"
                aria-label="Close"
              ></b-button>
            </div>
            <!-- end offcanvas-header-->

            <div class="offcanvas-body">
              <div>
                Some text as placeholder. In real life you can have the elements you have
                chosen. Like, text, images, lists, etc.
              </div>
              <h5 class="mt-3">List</h5>
              <ul class="ps-3">
                <li >Nemo enim ipsam voluptatem quia aspernatur</li>
                <li >Neque porro quisquam est, qui dolorem</li>
                <li >Quis autem vel eum iure qui in ea</li>
              </ul>
            </div>
            <!-- end offcanvas-body-->
          </div>
          <!-- end offcanvas-->
        </div>
      </div>
      <!-- end card-body card-buttons-->
    </div>
    <!-- end card-->
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
