<template>
  <div class="col-xl-6">
    <div class="card">
      <div class="card-body card-buttons">
        <h4 class="header-title">Bootstrap Modals</h4>

        <p>A rendered modal with header, body, and set of actions in the footer.</p>

        <!-- Standard modal content -->
        <div
          id="standard-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-labelledby="standard-modalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title" id="standard-modalLabel">Modal Heading</h4>
                <b-button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body">
                <h6>Text in a modal</h6>
                <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
                <hr />
                <h6>Overflowing text to show scroll behavior</h6>
                <p>
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                  dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
                  consectetur ac, vestibulum at eros.
                </p>
                <p>
                  Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                </p>
                <p>
                  Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus
                  magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec
                  ullamcorper nulla non metus auctor fringilla.
                </p>
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

        <!--  Modal content for the Large example -->
        <div
          class="modal fade"
          id="bs-example-modal-lg"
          tabindex="-1"
          role="dialog"
          aria-labelledby="myLargeModalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-lg">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title" id="myLargeModalLabel">Large modal</h4>
                <b-button
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body">...</div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <div
          class="modal fade"
          id="bs-example-modal-sm"
          tabindex="-1"
          role="dialog"
          aria-labelledby="mySmallModalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-sm">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title" id="mySmallModalLabel">Small modal</h4>
                <b-button
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body">...</div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <!-- Full width modal content -->
        <div
          id="full-width-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-labelledby="fullWidthModalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-full-width">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title" id="fullWidthModalLabel">Modal Heading</h4>
                <b-button
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body">
                <h6>Text in a modal</h6>
                <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
                <hr />
                <h6>Overflowing text to show scroll behavior</h6>
                <p>
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                  dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
                  consectetur ac, vestibulum at eros.
                </p>
                <p>
                  Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                </p>
                <p>
                  Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus
                  magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec
                  ullamcorper nulla non metus auctor fringilla.
                </p>
              </div>
              <div class="modal-footer">
                <b-button variant="light me-1" data-bs-dismiss="modal"> Close </b-button>
                <b-button variant="-primary"> Save changes </b-button>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <!-- Long Content Scroll Modal -->
        <div
          class="modal fade"
          id="scrollable-modal"
          tabindex="-1"
          role="dialog"
          aria-labelledby="scrollableModalTitle"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-dialog-scrollable" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="scrollableModalTitle">Modal title</h5>
                <b-button
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body">
                <p>
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                  dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
                  consectetur ac, vestibulum at eros.
                </p>
                <p>
                  Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                </p>
                <p>
                  Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus
                  magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec
                  ullamcorper nulla non metus auctor fringilla.
                </p>
                <p>
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                  dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
                  consectetur ac, vestibulum at eros.
                </p>
                <p>
                  Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                </p>
                <p>
                  Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus
                  magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec
                  ullamcorper nulla non metus auctor fringilla.
                </p>
                <p>
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                  dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
                  consectetur ac, vestibulum at eros.
                </p>
                <p>
                  Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                </p>
                <p>
                  Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus
                  magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec
                  ullamcorper nulla non metus auctor fringilla.
                </p>
                <p>
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                  dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
                  consectetur ac, vestibulum at eros.
                </p>
                <p>
                  Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                </p>
                <p>
                  Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus
                  magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec
                  ullamcorper nulla non metus auctor fringilla.
                </p>
                <p>
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                  dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
                  consectetur ac, vestibulum at eros.
                </p>
                <p>
                  Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                </p>
                <p>
                  Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus
                  magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec
                  ullamcorper nulla non metus auctor fringilla.
                </p>
                <p>
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
                  dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac
                  consectetur ac, vestibulum at eros.
                </p>
                <p>
                  Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                  Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                </p>
                <p>
                  Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus
                  magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec
                  ullamcorper nulla non metus auctor fringilla.
                </p>
              </div>
              <div class="modal-footer">
                <b-button variant="secondary me-1" data-bs-dismiss="modal">
                  Close
                </b-button>
                <b-button variant="primary"> Save changes </b-button>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <div class="button-list">
          <!-- Standard  modal -->
          <b-button
            variant="primary mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#standard-modal"
          >
            Standard Modal
          </b-button>
          <!-- Large modal -->
          <b-button
            variant="info mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#bs-example-modal-lg"
          >
            Large Modal
          </b-button>
          <!-- Small modal -->
          <b-button
            variant="success mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#bs-example-modal-sm"
          >
            Small Modal
          </b-button>
          <!-- Full width modal -->
          <b-button
            variant="primary mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#full-width-modal"
          >
            Full width Modal
          </b-button>
          <!-- Scrollable modal -->
          <b-button
            variant="secondary mt-1"
            data-bs-toggle="modal"
            data-bs-target="#scrollable-modal"
          >
            Scrollable Modal
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
