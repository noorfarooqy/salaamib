<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="page-header">
        <div class="content-page-header">
          <h5>Inbox</h5>
        </div>
      </div>
      <!-- /Page Header -->

      <div class="row">
        <div class="col-lg-3 col-md-4">
          <div class="card">
            <div class="card-body">
              <div class="compose-btn">
                <a href="javascript:void(0);" class="btn btn-primary btn-block w-100">
                  Compose
                </a>
              </div>
              <ul class="inbox-menu">
                <li class="active">
                  <a href="javascript:;"><i class="fas fa-download"></i> Inbox
                    <span class="mail-count">(5)</span></a>
                </li>
                <li>
                  <a href="javascript:;"><i class="far fa-star"></i> Important</a>
                </li>
                <li>
                  <a href="javascript:;"><i class="far fa-paper-plane"></i> Sent Mail</a>
                </li>
                <li>
                  <a href="javascript:;"><i class="far fa-file-alt"></i> Drafts
                    <span class="mail-count">(13)</span></a>
                </li>
                <li>
                  <a href="javascript:;" class="pb-0 mb-0"><i class="far fa-trash-alt"></i> Trash</a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-9 col-md-8">
          <div class="card bg-white">
            <div class="card-body">
              <div class="email-header">
                <div class="row">
                  <div class="col top-action-left">
                    <div class="float-left">
                      <div class="btn-group dropdown-action">
                        <button type="button" class="btn btn-white-outline dropdown-toggle me-1 mt-2"
                          data-bs-toggle="dropdown">
                          Select <i class="fas fa-angle-down"></i>
                        </button>
                        <div class="dropdown-menu">
                          <a class="dropdown-item" href="javascript:;">All</a>
                          <a class="dropdown-item" href="javascript:;">None</a>
                          <div class="dropdown-divider"></div>
                          <a class="dropdown-item" href="javascript:;">Read</a>
                          <a class="dropdown-item" href="javascript:;">Unread</a>
                        </div>
                      </div>
                      <div class="btn-group dropdown-action">
                        <button type="button" class="btn btn-white-outline dropdown-toggle me-1 mt-2"
                          data-bs-toggle="dropdown">
                          Actions <i class="fas fa-angle-down"></i>
                        </button>
                        <div class="dropdown-menu">
                          <a class="dropdown-item" href="javascript:;">Reply</a>
                          <a class="dropdown-item" href="javascript:;">Forward</a>
                          <a class="dropdown-item" href="javascript:;">Archive</a>
                          <div class="dropdown-divider"></div>
                          <a class="dropdown-item" href="javascript:;">Mark As Read</a>
                          <a class="dropdown-item" href="javascript:;">Mark As Unread</a>
                          <div class="dropdown-divider"></div>
                          <a class="dropdown-item" href="javascript:;">Delete</a>
                        </div>
                      </div>
                      <div class="btn-group dropdown-action">
                        <button type="button" class="btn btn-white-outline dropdown-toggle me-1 mt-2"
                          data-bs-toggle="dropdown">
                          <i class="fas fa-folder me-1"></i>
                          <i class="fas fa-angle-down"></i>
                        </button>
                        <div role="menu" class="dropdown-menu">
                          <a class="dropdown-item" href="javascript:;">Social</a>
                          <a class="dropdown-item" href="javascript:;">Forums</a>
                          <a class="dropdown-item" href="javascript:;">Updates</a>
                          <div class="dropdown-divider"></div>
                          <a class="dropdown-item" href="javascript:;">Spam</a>
                          <a class="dropdown-item" href="javascript:;">Trash</a>
                          <div class="dropdown-divider"></div>
                          <a class="dropdown-item" href="javascript:;">New</a>
                        </div>
                      </div>
                      <div class="btn-group dropdown-action">
                        <button type="button" data-bs-toggle="dropdown"
                          class="btn btn-white-outline dropdown-toggle me-1 mt-2">
                          <i class="fas fa-tags"></i> <i class="fas fa-angle-down"></i>
                        </button>
                        <div role="menu" class="dropdown-menu">
                          <a class="dropdown-item" href="javascript:;">Work</a>
                          <a class="dropdown-item" href="javascript:;">Family</a>
                          <a class="dropdown-item" href="javascript:;">Social</a>
                          <div class="dropdown-divider"></div>
                          <a class="dropdown-item" href="javascript:;">Primary</a>
                          <a class="dropdown-item" href="javascript:;">Promotions</a>
                          <a class="dropdown-item" href="javascript:;">Forums</a>
                        </div>
                      </div>
                      <div class="btn-group dropdown-action mail-search mt-2">
                        <input type="text" placeholder="Search Messages" class="form-control search-message" />
                      </div>
                    </div>
                  </div>
                  <div class="col-auto top-action-right">
                    <div class="text-end">
                      <button type="button" title="Refresh" data-toggle="tooltip"
                        class="btn btn-white-outline d-none d-md-inline-block me-1 mt-2">
                        <i class="fas fa-sync-alt"></i>
                      </button>
                      <div class="btn-group">
                        <a class="btn btn-white-outline"><i class="fas fa-angle-left"></i></a>
                        <a class="btn btn-white-outline"><i class="fas fa-angle-right"></i></a>
                      </div>
                    </div>
                    <div class="text-end">
                      <span class="text-muted d-none d-md-inline-block">Showing 10 of 112
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="email-content mt-2">
                <div class="table-responsive">
                  <table class="table table-inbox table-hover">
                    <thead>
                      <tr>
                        <th colspan="6" class="py-3">
                          <input type="checkbox" class="checkbox-all" />
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="unread clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="fas fa-star starred"></i></span>
                        </td>
                        <td class="name">John Doe</td>
                        <td class="subject">
                          Lorem ipsum dolor sit amet, consectetuer adipiscing elit
                        </td>
                        <td><i class="fas fa-paperclip"></i></td>
                        <td class="mail-date">13:14</td>
                      </tr>
                      <tr class="unread clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="far fa-star"></i></span>
                        </td>
                        <td class="name">Envato Account</td>
                        <td class="subject">
                          Important account security update from Envato
                        </td>
                        <td></td>
                        <td class="mail-date">8:42</td>
                      </tr>
                      <tr class="clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="far fa-star"></i></span>
                        </td>
                        <td class="name">Twitter</td>
                        <td class="subject">HRMS Bootstrap Admin Template</td>
                        <td></td>
                        <td class="mail-date">30 Nov</td>
                      </tr>
                      <tr class="unread clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="far fa-star"></i></span>
                        </td>
                        <td class="name">Richard Parker</td>
                        <td class="subject">
                          Lorem ipsum dolor sit amet, consectetuer adipiscing elit
                        </td>
                        <td></td>
                        <td class="mail-date">18 Sep</td>
                      </tr>
                      <tr class="clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="far fa-star"></i></span>
                        </td>
                        <td class="name">John Smith</td>
                        <td class="subject">
                          Lorem ipsum dolor sit amet, consectetuer adipiscing elit
                        </td>
                        <td></td>
                        <td class="mail-date">21 Aug</td>
                      </tr>
                      <tr class="clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="far fa-star"></i></span>
                        </td>
                        <td class="name">me, Robert Smith (3)</td>
                        <td class="subject">
                          Lorem ipsum dolor sit amet, consectetuer adipiscing elit
                        </td>
                        <td></td>
                        <td class="mail-date">1 Aug</td>
                      </tr>
                      <tr class="unread clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="far fa-star"></i></span>
                        </td>
                        <td class="name">Codecanyon</td>
                        <td class="subject">Welcome To Codecanyon</td>
                        <td></td>
                        <td class="mail-date">Jul 13</td>
                      </tr>
                      <tr class="clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="far fa-star"></i></span>
                        </td>
                        <td class="name">Richard Miles</td>
                        <td class="subject">
                          Lorem ipsum dolor sit amet, consectetuer adipiscing elit
                        </td>
                        <td><i class="fas fa-paperclip"></i></td>
                        <td class="mail-date">May 14</td>
                      </tr>
                      <tr class="unread clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="far fa-star"></i></span>
                        </td>
                        <td class="name">John Smith</td>
                        <td class="subject">
                          Lorem ipsum dolor sit amet, consectetuer adipiscing elit
                        </td>
                        <td></td>
                        <td class="mail-date">11/11/16</td>
                      </tr>
                      <tr class="clickable-row">
                        <td>
                          <input type="checkbox" class="checkmail" />
                        </td>
                        <td>
                          <span class="mail-important"><i class="far fa-star starred"></i></span>
                        </td>
                        <td class="name">Mike Litorus</td>
                        <td class="subject">
                          Lorem ipsum dolor sit amet, consectetuer adipiscing elit
                        </td>
                        <td></td>
                        <td class="mail-date">10/31/16</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Main Wrapper -->
</template>
