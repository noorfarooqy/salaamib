<template>
  <div class="card">
    <div class="card-body card-buttons">
      <h4 class="header-title">Offcanvas Backdrop</h4>
      <p>
        Scrolling the <code>&lt;body&gt;</code> element is disabled when an offcanvas and
        its backdrop are visible. Use the <code>data-bs-scroll</code> attribute to toggle
        <code>&lt;body&gt;</code> scrolling and <code>data-bs-backdrop</code> to toggle
        the backdrop.
      </p>

      <div class="button-list">
        <b-button
          variant="primary mt-2 me-1"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasScrolling"
          aria-controls="offcanvasScrolling"
        >
          Enable body scrolling
        </b-button>
        <b-button
          variant="primary mt-2 me-1"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasWithBackdrop"
          aria-controls="offcanvasWithBackdrop"
        >
          Enable backdrop (default)
        </b-button>
        <b-button
          variant="primary mt-2"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasWithBothOptions"
          aria-controls="offcanvasWithBothOptions"
        >
          Enable both scrolling & backdrop
        </b-button>
      </div>
      <!-- end button-list-->

      <div
        class="offcanvas offcanvas-start"
        data-bs-scroll="true"
        data-bs-backdrop="false"
        tabindex="-1"
        id="offcanvasScrolling"
        aria-labelledby="offcanvasScrollingLabel"
      >
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasScrollingLabel">
            Colored with scrolling
          </h5>
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

          <ul class="ps-3">
            <li >At vero eos et accusamus et iusto odio dignissimos</li>
            <li >Et harum quidem rerum facilis</li>
            <li >Temporibus autem quibusdam et aut officiis</li>
          </ul>
        </div>
        <!-- end offcanvas-body-->
      </div>
      <!-- end offcanvas-->

      <div
        class="offcanvas offcanvas-start"
        tabindex="-1"
        id="offcanvasWithBackdrop"
        aria-labelledby="offcanvasWithBackdropLabel"
      >
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasWithBackdropLabel">
            Offcanvas with backdrop
          </h5>
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

          <ul class="ps-3">
            <li >At vero eos et accusamus et iusto odio dignissimos</li>
            <li >Et harum quidem rerum facilis</li>
            <li >Temporibus autem quibusdam et aut officiis</li>
          </ul>
        </div>
        <!-- end offcanvas-body-->
      </div>
      <!-- end offcanvas-->

      <div
        class="offcanvas offcanvas-start"
        data-bs-scroll="true"
        tabindex="-1"
        id="offcanvasWithBothOptions"
        aria-labelledby="offcanvasWithBothOptionsLabel"
      >
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasWithBothOptionsLabel">
            Backdroped with scrolling
          </h5>
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

          <ul class="ps-3">
            <li >At vero eos et accusamus et iusto odio dignissimos</li>
            <li >Et harum quidem rerum facilis</li>
            <li >Temporibus autem quibusdam et aut officiis</li>
          </ul>
        </div>
        <!-- end offcanvas-body-->
      </div>
      <!-- end offcanvas-->
    </div>
    <!-- end card-body card-buttons-->
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
