<template>
  <div class="card">
    <div class="card-body card-buttons">
      <h4 class="header-title">Offcanvas</h4>
      <p>
        You can use a link with the <code>href</code> attribute, or a button with the
        <code>data-bs-target</code> attribute. In both cases, the
        <code>data-bs-toggle="offcanvas"</code> is required.
      </p>

      <div class="button-list">
        <a
          class="btn btn-primary mt-1 me-1"
          data-bs-toggle="offcanvas"
          href="#offcanvasExample"
          role="button"
          aria-controls="offcanvasExample"
        >
          Link with href
        </a>
        <b-button
          variant="primary mt-1"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasExample"
          aria-controls="offcanvasExample"
        >
          Button with data-bs-target
        </b-button>
      </div>
      <!-- end button-list-->

      <div
        class="offcanvas offcanvas-start"
        tabindex="-1"
        id="offcanvasExample"
        aria-labelledby="offcanvasExampleLabel"
      >
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasExampleLabel">Offcanvas</h5>
          <b-button
            type="button"
            class="btn-close text-reset mt-1"
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
