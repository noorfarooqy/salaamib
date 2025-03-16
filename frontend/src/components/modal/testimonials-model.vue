<template>
  <div class="modal custom-modal modal-lg fade" id="add_testimonial" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Add Testimonials</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-8 m-auto">
              <form action="javascript:;">
                <div class="card-body">
                  <div class="form-groups-item border-0 p-0">
                    <h5 class="form-title">Profile Picture</h5>
                    <div class="profile-picture">
                      <div class="upload-profile">
                        <div class="profile-img">
                          <img
                            id="blah"
                            class="avatar"
                            src="@/assets/img/profiles/avatar-10.jpg"
                            alt="profile-img"
                          />
                        </div>
                        <div class="add-profile">
                          <h5>Upload a New Photo</h5>
                          <span>Profile-pic.jpg</span>
                        </div>
                      </div>
                      <div class="img-upload">
                        <label class="btn btn-primary">
                          Upload <input type="file" />
                        </label>
                        <a class="btn btn-remove">Remove</a>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-12">
                        <div class="input-block mb-3">
                          <label>Name</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter Name"
                          />
                        </div>
                      </div>
                      <div class="col-lg-12">
                        <div class="input-block mb-3">
                          <label>Job Title</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter Job Title"
                          />
                        </div>
                      </div>
                      <div class="col-lg-4 col-md-6 col-sm-12">
                        <div class="input-block mb-3">
                          <label>Rating</label>
                          <div>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                          </div>
                        </div>
                      </div>
                      <div class="col-lg-12">
                        <div class="input-block">
                          <label>Comments</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter Comments"
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Add Testimonials</a
          >
        </div>
      </div>
    </div>
  </div>
  <!-- /Add Testmonials -->

  <!-- Edit Testmonials Modal -->
  <div class="modal custom-modal modal-lg fade" id="edit_testimonial" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-header border-0 pb-0">
          <div class="form-header modal-header-title text-start mb-0">
            <h4 class="mb-0">Edit Testimonials</h4>
          </div>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-lg-12 col-md-8 m-auto">
              <form action="javascript:;">
                <div class="card-body">
                  <div class="form-groups-item border-0 p-0">
                    <h5 class="form-title">Profile Picture</h5>
                    <div class="profile-picture">
                      <div class="upload-profile">
                        <div class="profile-img">
                          <img
                            id="blah1"
                            class="avatar"
                            src="@/assets/img/profiles/avatar-10.jpg"
                            alt="profile-img"
                          />
                        </div>
                        <div class="add-profile">
                          <h5>Upload a New Photo</h5>
                          <span>Profile-pic.jpg</span>
                        </div>
                      </div>
                      <div class="img-upload">
                        <label class="btn btn-primary">
                          Upload <input type="file" />
                        </label>
                        <a class="btn btn-remove">Remove</a>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-12">
                        <div class="input-block mb-3">
                          <label>Name</label>
                          <input
                            type="text"
                            class="form-control"
                            value="John Smith"
                            placeholder="Enter Name"
                          />
                        </div>
                      </div>
                      <div class="col-lg-12">
                        <div class="input-block mb-3">
                          <label>Job Title</label>
                          <input
                            type="text"
                            class="form-control"
                            value="Lorem ipsum dolor sit amet, consectetur"
                            placeholder="Enter Job Title"
                          />
                        </div>
                      </div>
                      <div class="col-lg-4 col-md-6 col-sm-12">
                        <div class="input-block mb-3">
                          <label>Rating</label>
                          <div>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                            <span class="mail-important"
                              ><i class="fas fa-star starred text-warning"></i
                            ></span>
                          </div>
                        </div>
                      </div>
                      <div class="col-lg-12">
                        <div class="input-block">
                          <label>Comments</label>
                          <input
                            type="text"
                            class="form-control"
                            value="Lorem ipsum dolor sit amet, consectetur"
                            placeholder="Enter Comments"
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-back cancel-btn me-2"
            >Cancel</a
          >
          <a href="javascript:;" data-bs-dismiss="modal" class="btn btn-primary paid-continue-btn"
            >Add Testimonials</a
          >
        </div>
      </div>
    </div>
  </div>
   <!-- Delete Items Modal -->
   <div class="modal custom-modal fade" id="delete_modal" role="dialog">
    <div class="modal-dialog modal-dialog-centered modal-md">
      <div class="modal-content">
        <div class="modal-body">
          <div class="form-header">
            <h3>Delete Testimonials</h3>
            <p>Are you sure want to delete?</p>
          </div>
          <div class="modal-btn delete-action">
            <div class="row">
              <div class="col-6">
                <button
                  type="reset"
                  data-bs-dismiss="modal"
                  class="w-100 btn btn-primary paid-continue-btn"
                >
                  Delete
                </button>
              </div>
              <div class="col-6">
                <button
                  type="submit"
                  data-bs-dismiss="modal"
                  class="w-100 btn btn-primary paid-cancel-btn"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Delete Items Modal -->
</template>
