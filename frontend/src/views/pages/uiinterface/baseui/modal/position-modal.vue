<template>
  <div class="col-xl-6">
    <div class="card">
      <div class="card-body card-buttons">
        <h4 class="header-title">Modal Position</h4>
        <p>
          Specify the position for the modal. You can display modal at top, bottom, center
          or right of page by specifying classes
          <code>modal-top</code>, <code>modal-bottom</code>,
          <code>modal-dialog-centered</code> and <code>modal-right </code> respectively.
        </p>

        <!-- Top modal content -->
        <div
          id="top-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-top">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title" id="topModalLabel">Modal Heading</h4>
                <b-button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body">
                <h5>Text in a modal</h5>
                <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
              </div>
              <div class="modal-footer">
                <b-button variant="light me-1" data-bs-dismiss="modal"> Close </b-button>
                <b-button variant="primary"> Save changes </b-button>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <!-- Right modal content -->
        <div
          id="right-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-sm modal-right">
            <div class="modal-content">
              <div class="modal-header border-0">
                <b-button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body">
                <div class="text-center">
                  <h4 class="mt-0">Text in a modal</h4>
                  <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
                  <b-button variant="danger btn-sm" data-bs-dismiss="modal">
                    Close
                  </b-button>
                </div>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <!-- Bottom modal content -->
        <div
          id="bottom-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-sm modal-bottom">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title" id="bottomModalLabel">Modal Heading</h4>
                <b-button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body">
                <h5>Text in a modal</h5>
                <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
              </div>
              <div class="modal-footer">
                <b-button variant="light me-1" data-bs-dismiss="modal"> Close </b-button>
                <b-button variant="primary"> Save changes </b-button>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <!-- Center modal content -->
        <div
          class="modal fade"
          id="centermodal"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title" id="myCenterModalLabel">Center modal</h4>
                <b-button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body">
                <h5>Overflowing text to show scroll behavior</h5>
                <p>
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                  dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
                  consectetur ac, vestibulum at eros.
                </p>
                <p>
                  Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                </p>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <div class="button-list">
          <!-- Top modal -->
          <b-button
            type="button"
            class="btn btn-secondary mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#top-modal"
          >
            Top Modal
          </b-button>
          <!-- Bottom modal -->
          <b-button
            variant="secondary mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#bottom-modal"
          >
            Bottom Modal
          </b-button>
          <!-- Center modal -->
          <b-button
            variant="secondary mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#centermodal"
          >
            Center modal
          </b-button>
          <!-- Right modal -->
          <b-button
            variant="secondary mt-1"
            data-bs-toggle="modal"
            data-bs-target="#right-modal"
          >
            Rightbar Modal
          </b-button>
        </div>
      </div>
      <!-- end card-body card-buttons -->
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
