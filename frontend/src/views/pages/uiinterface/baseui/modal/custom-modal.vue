<template>
  <div class="col-xl-6">
    <div class="card">
      <div class="card-body card-buttons">
        <h4 class="header-title">Custom Modals</h4>

        <p>Examples of custom modals.</p>

        <!-- sample modal content -->

        <div
          id="con-close-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-labelledby="myModalLabel"
          aria-hidden="true"
          style="display: none"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title">Modal Content is Responsive</h4>
                <b-button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></b-button>
              </div>
              <div class="modal-body p-4">
                <div class="row">
                  <div class="col-md-6">
                    <div class="mb-3">
                      <label for="field-1" class="form-label">Name</label>
                      <input
                        type="text"
                        class="form-control"
                        id="field-1"
                        placeholder="John"
                      />
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="mb-3">
                      <label for="field-2" class="form-label">Surname</label>
                      <input
                        type="text"
                        class="form-control"
                        id="field-2"
                        placeholder="Doe"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12">
                    <div class="mb-3">
                      <label for="field-3" class="form-label">Address</label>
                      <input
                        type="text"
                        class="form-control"
                        id="field-3"
                        placeholder="Address"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-4">
                    <div class="mb-3">
                      <label for="field-4" class="form-label">City</label>
                      <input
                        type="text"
                        class="form-control"
                        id="field-4"
                        placeholder="Boston"
                      />
                    </div>
                  </div>
                  <div class="col-md-4">
                    <div class="mb-3">
                      <label for="field-5" class="form-label">Country</label>
                      <input
                        type="text"
                        class="form-control"
                        id="field-5"
                        placeholder="United States"
                      />
                    </div>
                  </div>
                  <div class="col-md-4">
                    <div class="mb-3">
                      <label for="field-6" class="form-label">Zip</label>
                      <input
                        type="text"
                        class="form-control"
                        id="field-6"
                        placeholder="123456"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12">
                    <div >
                      <label for="field-7" class="form-label">Personal Info</label>
                      <textarea
                        class="form-control"
                        id="field-7"
                        placeholder="Write something about yourself"
                      ></textarea>
                    </div>
                  </div>
                </div>
              </div>
              <div class="modal-footer">
                <b-button variant="secondary waves-effect me-1" data-bs-dismiss="modal">
                  Close
                </b-button>
                <b-button variant="info waves-effect waves-light">
                  Save changes
                </b-button>
              </div>
            </div>
          </div>
        </div>
        <!-- /.modal -->

        <div
          id="accordion-modal"
          class="modal fade"
          tabindex="-1"
          role="dialog"
          aria-labelledby="myModalLabel"
          aria-hidden="true"
          style="display: none"
        >
          <div class="modal-dialog">
            <div class="modal-content p-0">
              <div id="accordion">
                <div class="card mb-0">
                  <div class="card-header" id="headingOne">
                    <h5 class="m-0">
                      <a
                        href="#collapseOne"
                        class="text-dark"
                        data-bs-toggle="collapse"
                        aria-expanded="true"
                        aria-controls="collapseOne"
                      >
                        Collapsible Group Item #1
                      </a>
                    </h5>
                  </div>

                  <div
                    id="collapseOne"
                    class="collapse show"
                    aria-labelledby="headingOne"
                    data-bs-parent="#accordion"
                  >
                    <div class="card-body card-buttons">
                      Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
                      terry richardson ad squid. 3 wolf moon officia aute, non cupidatat
                      skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod.
                      Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid
                      single-origin coffee nulla assumenda shoreditch et. Nihil anim
                      keffiyeh helvetica, craft beer labore wes anderson cred nesciunt
                      sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings
                      occaecat craft beer farm-to-table, raw denim aesthetic synth
                      nesciunt you probably haven't heard of them accusamus labore
                      sustainable VHS.
                    </div>
                  </div>
                </div>
                <div class="card mb-0">
                  <div class="card-header" id="headingTwo">
                    <h5 class="m-0">
                      <a
                        href="#collapseTwo"
                        class="collapsed text-dark"
                        data-bs-toggle="collapse"
                        aria-expanded="false"
                        aria-controls="collapseTwo"
                      >
                        Collapsible Group Item #2
                      </a>
                    </h5>
                  </div>
                  <div
                    id="collapseTwo"
                    class="collapse"
                    aria-labelledby="headingTwo"
                    data-bs-parent="#accordion"
                  >
                    <div class="card-body card-buttons">
                      Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
                      terry richardson ad squid. 3 wolf moon officia aute, non cupidatat
                      skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod.
                      Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid
                      single-origin coffee nulla assumenda shoreditch et. Nihil anim
                      keffiyeh helvetica, craft beer labore wes anderson cred nesciunt
                      sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings
                      occaecat craft beer farm-to-table, raw denim aesthetic synth
                      nesciunt you probably haven't heard of them accusamus labore
                      sustainable VHS.
                    </div>
                  </div>
                </div>
                <div class="card mb-0">
                  <div class="card-header" id="headingThree">
                    <h5 class="m-0">
                      <a
                        href="#collapseThree"
                        class="collapsed text-dark"
                        data-bs-toggle="collapse"
                        aria-expanded="false"
                        aria-controls="collapseThree"
                      >
                        Collapsible Group Item #3
                      </a>
                    </h5>
                  </div>
                  <div
                    id="collapseThree"
                    class="collapse"
                    aria-labelledby="headingThree"
                    data-bs-parent="#accordion"
                  >
                    <div class="card-body card-buttons">
                      Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
                      terry richardson ad squid. 3 wolf moon officia aute, non cupidatat
                      skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod.
                      Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid
                      single-origin coffee nulla assumenda shoreditch et. Nihil anim
                      keffiyeh helvetica, craft beer labore wes anderson cred nesciunt
                      sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings
                      occaecat craft beer farm-to-table, raw denim aesthetic synth
                      nesciunt you probably haven't heard of them accusamus labore
                      sustainable VHS.
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- /.modal-content -->
          </div>
          <!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->

        <div class="button-list">
          <!-- Responsive modal -->
          <b-button
            variant="success waves-effect waves-light mt-1 me-1"
            data-bs-toggle="modal"
            data-bs-target="#con-close-modal"
          >
            Responsive Modal
          </b-button>
          <!-- Accordion modal -->
          <b-button
            variant="secondary waves-effect waves-light mt-1"
            data-bs-toggle="modal"
            data-bs-target="#accordion-modal"
          >
            Accordion in Modal
          </b-button>
        </div>
      </div>
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
